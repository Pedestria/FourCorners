package pedestria.fourcorners.registry;

import java.util.function.Supplier;
import net.minecraft.world.item.BlockItem;
import net.minecraft.world.item.Item;
import net.minecraft.world.level.block.Block;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import pedestria.fourcorners.FourCorners;

public final class FCItems {
    public static final DeferredRegister<Item> ITEMS =
            DeferredRegister.create(ForgeRegistries.ITEMS, FourCorners.MODID);

    public static final RegistryObject<Item> START_TOME = registerSimpleItem("start_tome");
    public static final RegistryObject<Item> WISDOM_SHARD = registerSimpleItem("wisdom_shard");
    public static final RegistryObject<Item> AVALON_GEM = registerSimpleItem("avalon_gem");
    public static final RegistryObject<Item> WISDOM_INGOT = registerSimpleItem("wisdom_ingot");
    public static final RegistryObject<Item> AVALON_INGOT = registerSimpleItem("avalon_ingot");

    private FCItems() {}

    public static RegistryObject<Item> registerBlockItem(
            String name, Supplier<? extends Block> blockSupplier) {
        return ITEMS.register(name, () -> new BlockItem(blockSupplier.get(), new Item.Properties()));
    }

    private static RegistryObject<Item> registerSimpleItem(String name) {
        return ITEMS.register(name, () -> new Item(new Item.Properties()));
    }
}
