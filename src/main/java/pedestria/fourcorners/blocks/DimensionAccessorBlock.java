package pedestria.fourcorners.blocks;


import net.minecraft.block.ITileEntityProvider;
import net.minecraft.block.SoundType;
import net.minecraft.block.material.Material;
import net.minecraft.tileentity.TileEntity;
import net.minecraft.world.World;

public class DimensionAccessorBlock extends BlocksBase implements ITileEntityProvider {


	public DimensionAccessorBlock(String name, Material material) {
		super(name, material);

		setSoundType(SoundType.ANVIL);
		setHardness(3.0F);
		setResistance(20.0F);
		setHarvestLevel("pickaxe", 3);
		setLightLevel(7.0F);

	}

	@Override
	public TileEntity createNewTileEntity(World worldIn, int meta) {
		// TODO Auto-generated method stub
		return null;
	}

}
