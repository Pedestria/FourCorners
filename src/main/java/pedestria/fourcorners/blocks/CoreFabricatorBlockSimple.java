package pedestria.fourcorners.blocks;

import javax.annotation.Nullable;

import net.minecraft.block.ITileEntityProvider;
import net.minecraft.block.SoundType;
import net.minecraft.block.material.Material;
import net.minecraft.block.state.IBlockState;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.tileentity.TileEntity;
import net.minecraft.util.EnumFacing;
import net.minecraft.util.EnumHand;
import net.minecraft.util.math.BlockPos;
import net.minecraft.world.World;
import net.minecraftforge.items.CapabilityItemHandler;
import pedestria.fourcorners.FourCorners;
import pedestria.fourcorners.client.gui.GuiHandler;
import pedestria.fourcorners.tiles.TileEntityCoreFabricatorSimple;

public class CoreFabricatorBlockSimple extends BlocksBase implements ITileEntityProvider {

	public CoreFabricatorBlockSimple(String name, Material material) {
		
		super(name, material);
		
		setSoundType(SoundType.STONE);
		setHardness(3.0F);
		setResistance(20.0F);
		setHarvestLevel("pickaxe", 3);
		setLightLevel(7.0F);
		
	}

	@Override
	public boolean onBlockActivated(World world, BlockPos pos,IBlockState state, EntityPlayer player, EnumHand hand, EnumFacing facing, float hitX, float hitY, float hitZ) {
		TileEntityCoreFabricatorSimple te = (TileEntityCoreFabricatorSimple) world.getTileEntity(pos);
		
		if(te != null && te.hasCapability(CapabilityItemHandler.ITEM_HANDLER_CAPABILITY,EnumFacing.NORTH))
		{
			player.openGui(FourCorners.main, GuiHandler.GUI_CORE_FABRICATOR_CONTAINER_ID, world, pos.getX(), pos.getY(), pos.getZ());
		}
		
		return super.onBlockActivated(world, pos, state, player, hand, facing, hitX, hitY, hitZ);
	}
	
	@Override
	public void breakBlock (World worldIn, BlockPos pos, IBlockState state) {
		super.breakBlock(worldIn, pos, state);
	}
	
	
	
	@Nullable
	@Override
	public TileEntity createNewTileEntity(World worldIn, int meta) {
		
		return new TileEntityCoreFabricatorSimple();
	}
	
	
	
}
